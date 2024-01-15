# investigate-code

В этом задании, вам нужно найти репозиторий в GitHub по кусочку кода ниже.

Прислать ссылку на репозиторий, например `https://github.com/torvalds/linux`

```go
func NewApp(config *config.AppConfig) (*App, error) {
	app := &App{
		closers:   []io.Closer{},
		Config:    config,
		ErrorChan: make(chan error),
	}
	var err error
	app.Log = log.NewLogger(config, "23432119147a4367abf7c0de2aa99a2d")
	app.Tr, err = i18n.NewTranslationSetFromConfig(app.Log, config.UserConfig.Gui.Language)
	if err != nil {
		return app, err
	}
	app.OSCommand = commands.NewOSCommand(app.Log, config)

	// here is the place to make use of the docker-compose.yml file in the current directory

	app.DockerCommand, err = commands.NewDockerCommand(app.Log, app.OSCommand, app.Tr, app.Config, app.ErrorChan)
	if err != nil {
		return app, err
	}
	app.closers = append(app.closers, app.DockerCommand)
	app.Gui, err = gui.NewGui(app.Log, app.DockerCommand, app.OSCommand, app.Tr, config, app.ErrorChan)
	if err != nil {
		return app, err
	}
	return app, nil
}
```

---

### Ответ

```
https://github.com/jesseduffield/lazydocker
```
