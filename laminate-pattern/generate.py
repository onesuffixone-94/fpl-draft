# Generates laminate_pattern.svg  (retro rounded-rectangle pattern)
W, H = 1200, 1600          # artboard units (scale freely; vector)
THICK, THIN, R = 14, 2.5, 38
INK = "#000000"

# (x, y, w, h, dots) dots: None | 'l' | 'r'
thick = [
 (105,170,340,210,'r'), (565,130,185,310,'r'), (670,-60,350,270,None),
 (1035,255,200,215,None), (-10,575,330,305,'r'), (430,535,335,190,'r'),
 (795,565,165,265,'l'), (460,795,440,225,'r'), (1000,795,200,180,None),
 (-10,990,205,115,'r'), (-10,1195,170,145,'r'), (25,1300,195,180,'l'),
 (430,1058,225,160,None), (675,1212,280,185,None), (610,1370,145,180,None),
 (285,1462,240,150,'r'), (975,1135,115,175,'l'),
]
thin = [
 (800,230,200,280), (358,632,195,278), (975,627,180,138), (1055,430,200,255),
 (35,885,295,155), (835,870,110,115), (45,1120,275,155), (605,1070,175,215),
 (860,1072,103,108), (470,1265,190,245), (130,1375,205,240), (785,1385,160,180),
 (975,1375,125,145), (-60,210,145,355), (-50,-100,235,380), (375,-60,255,350),
 (725,1025,180,120),
]

o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
     '<title>Retro rounded-rectangle laminate pattern</title>',
     f'<defs><clipPath id="art"><rect width="{W}" height="{H}"/></clipPath></defs>',
     f'<rect id="bg" width="{W}" height="{H}" fill="none"/>',
     '<g clip-path="url(#art)" fill="none" stroke-linejoin="round">',
     f'<g id="thin-lines" stroke="{INK}" stroke-width="{THIN}">']
for x,y,w,h in thin:
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{R}"/>')
o.append('</g>')
o.append(f'<g id="thick-frames" stroke="{INK}" stroke-width="{THICK}">')
for x,y,w,h,d in thick:
    o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{R}"/>')
o.append('</g><g id="dotted-bands">')
for x,y,w,h,d in thick:
    if not d: continue
    bx = x+w-13 if d=='r' else x-13          # band centred on the edge
    o.append(f'<rect x="{bx}" y="{y+R-8}" width="26" height="{h-2*R+16}" fill="{INK}" stroke="none" rx="10"/>')
    cx = bx+13; n = int((h-2*R)//17)
    y0 = y+h/2-(n-1)*17/2
    o.append('<g fill="#ffffff" stroke="none">' +
             ''.join(f'<circle cx="{cx:.1f}" cy="{y0+i*17:.1f}" r="4.6"/>' for i in range(n)) + '</g>')
o.append('</g></g></svg>')
open('laminate_pattern.svg','w').write('\n'.join(o))
