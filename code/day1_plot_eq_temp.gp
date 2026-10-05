# day1_plot_eq_temp.gp
# 改造課題で作成したプログラムが出力する eq_temp.dat（1列目: S, 2列目: T）を可視化する。
# 使い方: gnuplot day1_plot_eq_temp.gp

set encoding utf8
set title "太陽定数 S と平衡温度 T の関係"
set xlabel "太陽定数 S [W/m^2]"
set ylabel "平衡温度 T [K]"
set grid
set key left top

plot "eq_temp.dat" using 1:2 with lines lw 2 title "T(S)  (albedo=0.30)"

pause -1 "何かキーを押すと終了します"
