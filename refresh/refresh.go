package refresh

import "time"

// Escolhendo a velocidade de atualização de tela
func RefreshRate(fps int) float64 {
	return 1.0 / float64(fps) * float64(time.Second)
}
