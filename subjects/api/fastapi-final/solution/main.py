from datetime import datetime
from fastapi import FastAPI, Header, Response, Request
from prometheus_client import Counter, Gauge, Histogram, make_asgi_app
from pydantic import BaseModel


app = FastAPI()

LAST_SUM1N = Gauge('last_sum1n', 'Value stores last result of sum1n')
LAST_FIBO = Gauge('last_fibo', 'Value stores last result of fibo')
LIST_SIZE = Gauge('list_size', 'Value stores current list size')
LAST_CALCULATOR = Gauge('last_calculator', 'Value stores last result of calculator')
ERRORS_CALCULATOR_TOTAL = Counter('errors_calculator_total', 'Number of errors in calculator')

HTTP_REQUESTS_TOTAL = Counter('http_requests_total', 'Number of HTTP requests received', ['method', 'endpoint'])
HTTP_REQUESTS_SECONDS = Histogram('http_requests_seconds', 'Duration of HTTP requests in seconds', ['method', 'endpoint'])

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = datetime.now()
    response = await call_next(request)
    process_time = int((datetime.now() - start_time).total_seconds() * 1000)
    HTTP_REQUESTS_TOTAL.labels(request.method, request.url.path).inc()
    HTTP_REQUESTS_SECONDS.labels(request.method, request.url.path).observe(process_time)
    return response

@app.get("/sum1n/{n}")
def sum1n(n: int):
    result = {"result": (n*(n+1))/2}
    LAST_SUM1N.set((n*(n+1))/2)
    return result

def calc_fib(n: int):
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n-1]

@app.get("/fibo")
def fibo(n: int):
    LAST_FIBO.set(calc_fib(n))
    return {"result": calc_fib(n)}

@app.post("/reverse")
def reverse(string: str = Header(None)):
    return {"result": string[::-1]}


class ListBody(BaseModel):
    element: str

global_list = []

@app.put("/list")
def list_patch(body: ListBody):
    global_list.append(body.element)
    LIST_SIZE.set(len(global_list))

@app.get("/list")
def list_get():
    return {"result": global_list}

class СalculatorBody(BaseModel):
    expr: str

@app.post("/calculator")
def calculator(body: СalculatorBody, response: Response):
    if len(body.expr.split(",")) != 3:
        response.status_code = 400
        return {"error": "invalid"}
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    s_num1, s_op, s_num2 = body.expr.split(",")
    try:
        num1 = int(s_num1)
        num2 = int(s_num2)
        if s_op not in ops:
            raise Exception(s_op)
    except Exception:
        response.status_code = 400
        ERRORS_CALCULATOR_TOTAL.inc()
        return {"error": "invalid"}
    try:
        data = {"result": ops[s_op](num1, num2)}
        LAST_CALCULATOR.set(ops[s_op](num1, num2))
        return data
    except ZeroDivisionError:
        response.status_code = 403
        ERRORS_CALCULATOR_TOTAL.inc()
        return {"error": "zerodiv"}
