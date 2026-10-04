# day2_plot_ebm_time.gp
# 改造課題で作成したプログラムが出力する ebm_time.dat（1列目: t, 2列目: T）を可視化する。
# 使い方: gnuplot day2_plot_ebm_time.gp

set title "温度の時間発展 (Euler法)"
set xlabel "時刻 t [s]"
set ylabel "温度 T [K]"
set grid
set key right bottom

plot "ebm_time.dat" using 1:2 with lines lw 2 title "放射収支モデル T(t)"

pause -1 "何かキーを押すと終了します"
