#!/usr/bin/env python3
"""Sơ đồ kết nối Nút bấm + Buzzer với Arduino"""

import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=13, unit=3)

    # === Mạch 1: Nút bấm (dùng INPUT_PULLUP) ===
    d += elm.Dot(open=True).at((0, 0)).label('Arduino Chân 2', loc='left')
    d += elm.Line().right().length(1)
    d += elm.Button().right().label('Nút bấm')
    d += elm.Line().down().length(1.5)
    d += elm.Ground().label('GND')

    # === Mạch 2: Buzzer ===
    d += (spk := elm.Speaker().at((3, -5)).right().label('Buzzer'))
    d += elm.Dot(open=True).at((0, -5)).label('Arduino Chân 8', loc='left')
    d += elm.Line().right().to(spk.in1)
    d += elm.Line().at(spk.in2).down().length(1)
    d += elm.Ground().label('GND')

    d.save('arduino-robot-thcs/du-an-2-chuong-cua/so-do-ket-noi-buzzer.svg')
    print("✅ Saved")
