package main

import (
	"github.com/veandco/go-sdl2/sdl"
)

func main() {
	if err := sdl.Init(sdl.INIT_EVERYTHING); err != nil {
		panic(err)
	}
	defer sdl.Quit()

	janela, err := sdl.CreateWindow("Trabalho prático 1", sdl.WINDOWPOS_CENTERED, sdl.WINDOWPOS_CENTERED,
		800, 600, sdl.WINDOW_SHOWN)
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

		DesenharPontoBranco(janela, superficie, mouseX, mouseY)
		if estado&sdl.Button(sdl.BUTTON_LEFT) == 0 {
			superficie.FillRect(nil, 0)
		}
	}
}

// Retornar um ponto branco
func DesenharPontoBranco(janela *sdl.Window, superficie *sdl.Surface, X int32, Y int32) {
	superficie.FillRect(&sdl.Rect{X, Y, 30, 30}, 0xffffffff)
	janela.UpdateSurface()
}

// Desenhar linha usando algoritmo de Bresenhan
func Brensenhan() {

}
