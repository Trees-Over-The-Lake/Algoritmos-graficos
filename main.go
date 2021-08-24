package main

import (
	"graphics_algorithms/algorithms"
	"graphics_algorithms/refresh"

	"github.com/veandco/go-sdl2/sdl"
)

func main() {
	if err := sdl.Init(sdl.INIT_EVERYTHING); err != nil {
		panic(err)
	}
	defer sdl.Quit()

	janela, err := sdl.CreateWindow("Trabalho prático 1", sdl.WINDOWPOS_CENTERED, sdl.WINDOWPOS_CENTERED,
		1280, 720, sdl.WINDOW_SHOWN)
	if err != nil {
		panic(err)
	}
	defer janela.Destroy()

	superficie, err := janela.GetSurface()
	if err != nil {
		panic(err)
	}
	superficie.FillRect(nil, 0)

	running := true
	for running {
		for event := sdl.PollEvent(); event != nil; event = sdl.PollEvent() {
			switch event.(type) {
			case *sdl.QuitEvent:
				println("Quit")
				running = false
			}
		}

		// Pegar a ultima atualização dos inputs
		sdl.PumpEvents()
		// Pegando a posição do mouse na tela
		mouseX, mouseY, estado := sdl.GetMouseState()

		if estado&sdl.Button(sdl.BUTTON_LEFT) == 1 {
			superficie.FillRect(nil, 0)
			algorithms.DDA(janela, superficie, 50, 50, int(mouseX), int(mouseY))
			algorithms.DDA(janela, superficie, int(mouseX), int(mouseY), 500, 500)
			algorithms.DDA(janela, superficie, 500, 500, 50, 50)
		}

		// Sincronização vertical do monitor com a aplicação
		refresh.Vsync(janela)
	}
}
