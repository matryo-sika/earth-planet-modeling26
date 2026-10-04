# day2_plot_cooling.gp
# day2_newton_cooling.c が出力する cooling.dat を可視化する。
# dt を変えて再実行し、結果を比較してみよう。
# 使い方: gnuplot day2_plot_cooling.gp

set title "ニュートンの冷却則 (Euler法)"
set xlabel "時刻 t [s]"
set ylabel "温度 T [K]"
set grid

plot "cooling.dat" using 1:2 with linespoints lw 2 pt 7 ps 0.5 title "T(t)"

pause -1 "何かキーを押すと終了します"
