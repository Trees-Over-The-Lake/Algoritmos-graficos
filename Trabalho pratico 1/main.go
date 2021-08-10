package main

import (
	"runtime"

	"github.com/go-gl/glfw/v3.3/glfw"
)

func init() {
	runtime.LockOSThread() // Algumas operacoes precisam ser executadas obrigatoriamente na thread main
}

func main() {
	err := glfw.Init()
	if err != nil {
		panic(err)
	}
	defer glfw.Terminate()

	window, err := glfw.CreateWindow(640, 480, "Trabalho prático 1", nil, nil)
	if err != nil {
		panic(err)
	}

	window.MakeContextCurrent()

	for !window.ShouldClose() {
		// Inicializar janela
		window.SwapBuffers()
		glfw.PollEvents()
	}
}
