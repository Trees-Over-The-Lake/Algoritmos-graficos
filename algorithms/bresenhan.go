package algorithms

import (
	"math"

	"github.com/veandco/go-sdl2/sdl"
)

// Desenhar linha usando algoritmo de Bresenhan
func Brensenhan(janela *sdl.Window, superficie *sdl.Surface, X1 int, Y1 int, X2 int, Y2 int) {
	var dx, dy, x, y, const1, const2, p int

	dx = int(math.Abs(float64(X2) - float64(X1)))
	dy = int(math.Abs(float64(Y2) - float64(Y1)))

	p = 2*dy - dx
	const1 = 2 * dy
	const2 = 2 * (dy - dx)
	x = X1
	y = Y1

	DesenharPontoBranco(janela, superficie, int32(x), int32(y))
	for x < X2 {
		x = x + 1

		if p < 0 {
			p += const1

		} else {
			p += const2
			y++
		}

		DesenharPontoBranco(janela, superficie, int32(x), int32(y))
	}
}
