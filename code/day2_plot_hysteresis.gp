# day2_plot_hysteresis.gp
# 発展課題で作成したプログラムが出力する hysteresis_up.dat, hysteresis_down.dat
# （各ファイル 1列目: S, 2列目: T）を可視化する。
# 使い方: gnuplot day2_plot_hysteresis.gp

set title "氷アルベドフィードバックによるヒステリシス"
set xlabel "太陽定数 S [W/m^2]"
set ylabel "平衡温度 T [K]"
set grid
set key left top

plot "hysteresis_up.dat"   using 1:2 with lines lw 2 title "Sを増加させた場合", \
     "hysteresis_down.dat" using 1:2 with lines lw 2 title "Sを減少させた場合"

pause -1 "何かキーを押すと終了します"
