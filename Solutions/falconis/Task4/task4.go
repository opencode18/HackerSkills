package main

import (
	"math"

	"github.com/Arafatk/glot"
)

func main() {
	dimensions := 2
	// The dimensions supported by the plot
	persist := false
	debug := false
	plot, _ := glot.NewPlot(dimensions, persist, debug)
	pointGroupName := "Sine Wave"
	var x []float64
	j := 0.0
	for i := 0; i < 10000; i++ {
		x = append(x, j)
		j += 0.0001
	}
	var y []float64
	for i := 0; i < 10000; i++ {
		y = append(y, math.Sin(x[i]*2*math.Pi))
	}
	style := "lines"
	points := [][]float64{x, y}
	plot.AddPointGroup(pointGroupName, style, points)
	plot.SetTitle("Sine Plot")
	plot.SetYrange(-2, 2)
	plot.SetXLabel("X-Axis(2* pi * x)")
	plot.SetYLabel("Y-Axis")
	plot.SavePlot("sine_go.png")
	// pointGroupName := "Simple Circles"
	// style := "circle"
	// points := [][]float64{{7, 3, 13, 5.6, 11.1}, {12, 13, 11, 1, 7}}
	// // Adding a point group
	// plot.AddPointGroup(pointGroupName, style, points)
	// pointGroupName = "Simple Lines"
	// style = "lines"
	// points = [][]float64{{7, 3, 3, 5.6, 5.6, 7, 7, 9, 13, 13, 9, 9}, {10, 10, 4, 4, 5.4, 5.4, 4, 4, 4, 10, 10, 4}}
	// plot.AddPointGroup(pointGroupName, style, points)
	// // A plot type used to make points/ curves and customize and save them as an image.
	// // plot.SetTitle("Example Plot")
	// // // Optional: Setting the title of the plot
	// // plot.SetXLabel("X-Axis")
	// // plot.SetYLabel("Y-Axis")
	// // // Optional: Setting label for X and Y axis
	// // plot.SetXrange(-2, 18)
	// // plot.SetYrange(-2, 18)
	// // // Optional: Setting axis ranges
	// plot.SavePlot("2.png")
}
