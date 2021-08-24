package refresh

import (
	"time"

	"github.com/veandco/go-sdl2/sdl"
)

// Escolhendo a velocidade de atualização de tela
func refreshRate(fps int) float64 {
	return 1.0 / float64(fps) * float64(time.Microsecond)
}

// Vsync
func Vsync(tela *sdl.Window) {
	modosTela, err := tela.GetDisplayMode()
	if err != nil {
		panic(err)
	}

	sdl.Delay(uint32(refreshRate(int(modosTela.RefreshRate))))
}
