# day3_plot_energy.gp
# orbit_euler.dat, orbit_leapfrog.dat の6列目（力学的エネルギー）を比較し、
# Euler法ではエネルギーがずれていくのに対し、リープ・フロッグ法では
# ほぼ一定に保たれることを確認する。
# 使い方: gnuplot day3_plot_energy.gp

set title "力学的エネルギー(単位質量あたり)の時間変化"
set xlabel "時刻 t [s]"
set ylabel "エネルギー [J/kg]"
set grid
set key outside

plot "orbit_euler.dat"  using 1:6 with lines lw 2 title "Euler法", \
     "orbit_leapfrog.dat" using 1:6 with lines lw 2 title "リープ・フロッグ法"

pause -1 "何かキーを押すと終了します"
