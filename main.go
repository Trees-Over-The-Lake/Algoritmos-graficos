package main

import (
	"graphics_algorithms/algorithms"
	"graphics_algorithms/geometricshapes"
	"graphics_algorithms/refresh"
	"time"

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

	// Creating a triangle
	triangle := geometricshapes.New()

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

			if triangle.X1 == -1 {
				triangle.X1 = int(mouseX)
				triangle.Y1 = int(mouseY)

				// Confirming the input
				algorithms.DesenharPontoBranco(superficie, int32(triangle.X1), int32(triangle.Y1))

			} else if triangle.X2 == -1 {
				triangle.X2 = int(mouseX)
				triangle.Y2 = int(mouseY)

				// Confirming the input
				algorithms.DesenharPontoBranco(superficie, int32(triangle.X2), int32(triangle.Y2))

			} else if triangle.X3 == -1 {
				triangle.X3 = int(mouseX)
				triangle.Y3 = int(mouseY)

				// Draw the triangle after getting the 3 positions
				triangle.Draw(superficie)

			} else {
				superficie.FillRect(nil, 0)
				triangle.Clear()
			}

			time.Sleep(150 * time.Millisecond)
		}

		// Sincronização vertical do monitor com a aplicação
		refresh.Vsync(janela)
		janela.UpdateSurface()
	}
}
