package main

import (
	"fmt"
	"runtime"
	"time"

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

	// // OR using GLFW:
	// vk.SetGetInstanceProcAddr(glfw.GetVulkanGetInstanceProcAddress())

	// if err := vk.Init(); err != nil {
	// 	panic(err)
	// }

	janela, err := glfw.CreateWindow(1280, 720, "Trabalho prático 1", nil, nil)
	if err != nil {
		panic(err)
	}

	janela.MakeContextCurrent()

	for !janela.ShouldClose() {
		// Inicializar janela
		if janela.GetMouseButton(glfw.MouseButton1) == glfw.Press {
			posX, posY := janela.GetCursorPos()
			fmt.Printf("Posição X: %v | Posição Y: %v\n", posX, posY)
			time.Sleep(time.Millisecond * 250)
		}

		janela.SwapBuffers()
		glfw.PollEvents()

	}
}
