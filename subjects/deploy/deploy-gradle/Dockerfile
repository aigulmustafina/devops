FROM ubuntu:18.04

ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y curl wget git openjdk-8-jdk unzip

RUN wget https://services.gradle.org/distributions/gradle-6.4.1-bin.zip -P /tmp
RUN unzip -d /opt/gradle /tmp/gradle-*.zip

ENV GRADLE_HOME=/opt/gradle/gradle-6.4.1

RUN git clone https://github.com/jusan-singularity/gradle-spring-rest /app
WORKDIR /app
RUN /opt/gradle/gradle-6.4.1/bin/gradle clean build

CMD ["java", "-jar", "build/libs/spring-boot-gradle-example-1.0.0.jar"]
# CMD ["sleep", "100000"]
