# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:13:59 2021

@author: pc
"""

def score():
    Q = 0
    W = int(input("주차 수: "))
    for E in range(1,W+1):
        a = float(input("%d주차 과제의 점수: "%(E)))
        Q+=a
   
    M_test = int(input("중간고사 성적"))
    F_test = int(input("기말고사 성적"))
    


    A = Q/W * 0.4                                         
    M = M_test * 0.3
    F = F_test * 0.3



    total = A + M + F
    if 100 >= total >= 90:
        grade = "A"
    elif 90 > total >= 80:
        grade = "B"
    elif 80 > total >= 70:
        grade = "C"
    elif 70 > total >= 60:
        grade = "D"
    elif total < 60:
        grade = "F"
    
    
    print("\n총점이 %d점이므로"%Q)
    print("주차별 과제의 평균은 %.2f점입니다."%(Q/W))
    print("과제 반영점수(40%)" ,A , "중간 반영점수(30%)" , M, "기말 반영점수(30%)" , F)
    print("성적은" + grade + "입니다.")

score()