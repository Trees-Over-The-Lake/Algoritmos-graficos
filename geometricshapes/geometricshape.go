package geometricshapes

import (
	"graphics_algorithms/algorithms"

	"github.com/veandco/go-sdl2/sdl"
)

// Saving all necessery positions to make a triangle
type Triangle struct {
	X1, X2, X3 int
	Y1, Y2, Y3 int
}

// Creating object
func New() Triangle {
	var t Triangle
	t.X1 = -1
	t.X2 = -1
	t.X3 = -1
	t.Y1 = -1
	t.Y2 = -1
	t.Y3 = -1
	return t
}

// Drawing the triangle
func (t *Triangle) Draw(superficie *sdl.Surface) {
	algorithms.DDA(superficie, t.X1, t.Y1, t.X2, t.Y2)
	algorithms.DDA(superficie, t.X2, t.Y2, t.X3, t.Y3)
	algorithms.DDA(superficie, t.X3, t.Y3, t.X1, t.Y1)
}

// Cleaning all the posicions
func (t *Triangle) Clear() {
	t.X1 = -1
	t.X2 = -1
	t.X3 = -1
	t.Y1 = -1
	t.Y2 = -1
	t.Y3 = -1
}
