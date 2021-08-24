package algorithms

import (
	"math"

	"github.com/veandco/go-sdl2/sdl"
)

// Algoritmo DDA
func DDA(X1 int, Y1 int, X2 int, Y2 int, janela *sdl.Window, superficie *sdl.Surface) {
	var dx, dy, passos int
	var x_incr, y_incr, x, y float64

	// Início do algoritmo
	dx = X2 - X1
	dy = Y2 - Y1

	if math.Abs(float64(dx)) > math.Abs(float64(dy)) {
		passos = int(math.Abs(float64(dx)))

	} else {
		passos = int(math.Abs(float64(dy)))

	}

	x_incr = float64(dx) / float64(passos)
	y_incr = float64(dy) / float64(passos)
	x = float64(X1)
	y = float64(Y1)

	DesenharPontoBranco(janela, superficie, int32(math.Round(x)), int32(math.Round(y)))

	for i := 1; i < passos; i++ {
		x += x_incr
		y += y_incr
		DesenharPontoBranco(janela, superficie, int32(math.Round(x)), int32(math.Round(y)))
	}
}
