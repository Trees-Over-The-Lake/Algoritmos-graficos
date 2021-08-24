package algorithms

import "github.com/veandco/go-sdl2/sdl"

// Retornar um ponto branco
func DesenharPontoBranco(janela *sdl.Window, superficie *sdl.Surface, X int32, Y int32) {
	superficie.FillRect(&sdl.Rect{X, Y, 10, 10}, 0xffffffff)
	janela.UpdateSurface()
}
