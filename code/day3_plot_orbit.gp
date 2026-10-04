# day3_plot_orbit.gp
# 改造課題で作成した2つのプログラムが出力する
# orbit_euler.dat, orbit_leapfrog.dat（2列目: x, 3列目: y）を重ねて表示し、
# 軌道の形の違いを比較する。
# 使い方: gnuplot day3_plot_orbit.gp

set title "地球の軌道: Euler法 vs リープ・フロッグ法"
set xlabel "x [m]"
set ylabel "y [m]"
set size ratio -1
set grid
set key outside

plot "orbit_euler.dat"  using 2:3 with lines lw 2 title "Euler法", \
     "orbit_leapfrog.dat" using 2:3 with lines lw 2 title "リープ・フロッグ法"

pause -1 "何かキーを押すと終了します"
