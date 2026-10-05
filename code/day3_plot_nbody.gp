# day3_plot_nbody.gp
# 発展課題で作成したプログラムが出力する nbody.dat（太陽・地球・木星）を可視化する。
# 使い方: gnuplot day3_plot_nbody.gp

set encoding utf8
set title "太陽・地球・木星の軌道 (N体シミュレーション, リープ・フロッグ法)"
set xlabel "x [m]"
set ylabel "y [m]"
set size ratio -1
set grid
set key outside

plot "nbody.dat" using 2:3 with lines lw 2 title "太陽", \
     "nbody.dat" using 4:5 with lines lw 2 title "地球", \
     "nbody.dat" using 6:7 with lines lw 2 title "木星"

pause -1 "何かキーを押すと終了します"
