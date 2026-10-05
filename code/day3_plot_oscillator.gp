# day3_plot_oscillator.gp
# day3_oscillator_euler.c が出力する oscillator.dat を可視化する。
# 位置 x(t) とエネルギーの時間変化を2枚並べて表示する。
# 使い方: gnuplot day3_plot_oscillator.gp

set encoding utf8
set multiplot layout 2,1
set grid

set title "単振動: 位置 x(t)  (Euler法)"
set xlabel "時刻 t"
set ylabel "位置 x"
plot "oscillator.dat" using 1:2 with lines lw 2 title "x(t)"

set title "力学的エネルギーの時間変化 (本来は一定のはず)"
set xlabel "時刻 t"
set ylabel "エネルギー"
plot "oscillator.dat" using 1:4 with lines lw 2 lc rgb "red" title "エネルギー"

unset multiplot
pause -1 "何かキーを押すと終了します"
