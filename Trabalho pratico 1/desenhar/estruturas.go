package desenhar

// Um ponto na matriz da tela
type Ponto struct {
	X1 uint32 // Referente a altura
	X2 uint32 // Referente a largura
	Yl uint32 // Referente a altura
	Y2 uint32 // Referente a largura
}

func criarLinha(X1 uint32, X2 uint32, Y1 uint32, Y2 uint32) *Ponto {
	var p Ponto

	p.X1 = X1
	p.X2 = X2
	p.Yl = Y1
	p.Y2 = Y2

	return &p
}

// Um conjunto de pontos para formar um objeto
type Pontos struct {
	P []Ponto
}
