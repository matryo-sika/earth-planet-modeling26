/*
 * day3_oscillator_euler.c
 * 第3回: Euler法の確認（もう一度）
 *
 * 単振動  d^2x/dt^2 = -(k/m) x  を1階の連立常微分方程式
 *   dx/dt = v
 *   dv/dt = -(k/m) x
 * に直し、陽的Euler法で解く。位置エネルギーと運動エネルギーの
 * 合計（力学的エネルギー）も一緒に出力し、Euler法だと
 * エネルギーが少しずつ増えてしまう（=不安定）ことを確認する。
 *
 * このあとの重力2体問題も、まったく同じ構造
 * （加速度を計算 → 速度を更新 → 位置を更新）で書ける。
 */
#include <stdio.h>

int main(void)
{
    double k = 1.0;   /* ばね定数 */
    double m = 1.0;   /* 質量 */
    double x = 1.0;   /* 初期位置 */
    double v = 0.0;   /* 初期速度 */

    double dt = 0.01;
    int nsteps = 3000;

    FILE *fp = fopen("oscillator.dat", "w");
    if (fp == NULL) {
        fprintf(stderr, "output file cannot be opened.\n");
        return 1;
    }

    fprintf(fp, "# t  x  v  energy\n");
    double t = 0.0;
    for (int i = 0; i <= nsteps; i++) {
        double energy = 0.5 * m * v * v + 0.5 * k * x * x;
        fprintf(fp, "%.4f %.6f %.6f %.6f\n", t, x, v, energy);

        double a = -(k / m) * x;      /* 加速度 = 力 / 質量 */

        double x_new = x + dt * v;    /* Euler法: 古い v で x を更新 */
        double v_new = v + dt * a;    /* Euler法: 古い a で v を更新 */

        x = x_new;
        v = v_new;
        t = t + dt;
    }

    fclose(fp);
    printf("oscillator.dat を出力しました。\n");
    return 0;
}
