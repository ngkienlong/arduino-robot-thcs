#!/usr/bin/env python3
"""Sơ đồ kết nối Nút bấm + Buzzer với Arduino"""

import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=13, unit=3)

    # === Mạch 1: Nút bấm (dùng INPUT_PULLUP) ===
    # Arduino chân 2 → nút bấm → GND
    d += (pin2 := elm.Dot(open=True).label('Arduino\nChân 2', loc='left'))
    d += elm.Line().right().length(1.5)
    d += elm.Button().right().label('Nút bấm')
    d += elm.Line().right().length(1.5)
    d += elm.Ground().label('GND')

    # === Mạch 2: Buzzer ===
    # Arduino chân 8 → buzzer → GND
    d += (pin8 := elm.Dot(open=True).at((0, -4)).label('Arduino\nChân 8', loc='left'))
    d += elm.Line().right().length(1.5)
    d += elm.Speaker().right().label('Buzzer')
    d += elm.Line().right().length(1.5)
    d += elm.Ground().label('GND')

    # Ghi chú
    d += elm.Label().at((3, -7)).label(
        'Nút bấm dùng INPUT_PULLUP\n(không cần điện trở ngoài)',
        fontsize=10
    )

    d.save('arduino-robot-thcs/du-an-2-chuong-cua/so-do-ket-noi-buzzer.svg')
    print("✅ Saved so-do-ket-noi-buzzer.svg")
