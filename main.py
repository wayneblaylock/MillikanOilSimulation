import pygame

pygame.init()


def ResizeMath(w, h):
    if h*4 > w*3:
        return((int(0), int((h-(w*3/4))/2), int(w), int(w*3/4)))
    else:
        return((int((w-(h*4/3))/2), int(0), int(h*4/3), int(h)))

def DrawSegment(surface, i, width, height):
    color1 = color2 = color3 = color4 = color5 = color6 = color7 = (30,30,30)

    red = (200,0,0)

    if i == 0: color1 = color2 = color3 = color4 = color5 = color6 = red
    elif i == 1: color2 = color3 = red
    elif i == 2: color1 = color2 = color7 = color5 = color4 = red
    elif i == 3: color1 = color2 = color7 = color3 = color4 = red
    elif i == 4: color6 = color7 = color2 = color3 = red
    elif i == 5: color1 = color6 = color7 = color3 = color4 = red
    elif i == 6: color1 = color6 = color5 = color4 = color3 = color7 = red
    elif i == 7: color1 = color2 = color3 = red
    elif i == 8: color1 = color2 = color3 = color4 = color5 = color6 = color7 = red
    elif i == 9: color7 = color6 = color1 = color2 = color3 = red

    pygame.draw.polygon(surface, color1, [(.05*height,.05*height),(.1*height,0),(width-.1*height,0),(width-.05*height, .05*height),(width-.1*height,.1*height),(.1*height,.1*height)])
    pygame.draw.polygon(surface, color2, [(width-.05*height, .08*height), (width, .13*height), (width, .42*height), (width-.05*height, .47*height), (width-.1*height, .42*height), (width-.1*height, .13*height)])
    pygame.draw.polygon(surface, color3, [(width-.05*height, .53*height), (width, .58*height), (width, .87*height), (width-.05*height, .92*height), (width-.1*height, .87*height), (width-.1*height, .58*height)])
    pygame.draw.polygon(surface, color4, [(.05*height,.95*height),(.1*height,.9*height),(width-.1*height,.9*height),(width-.05*height, .95*height),(width-.1*height,height),(.1*height,height)])
    pygame.draw.polygon(surface, color5, [(.05*height, .53*height), (.1*height, .58*height), (.1*height, .87*height), (.05*height, .92*height), (0, .87*height), (0, .58*height)])
    pygame.draw.polygon(surface, color6, [(.05*height, .08*height), (.1*height, .13*height), (.1*height, .42*height), (.05*height, .47*height), (0, .42*height), (0, .13*height)])
    pygame.draw.polygon(surface, color7, [(.05*height,.5*height),(.1*height,.45*height),(width-.1*height,.45*height),(width-.05*height, .5*height),(width-.1*height,.55*height),(.1*height,.55*height)])

def IntToString(v):
    #if v < 0.1: return "000.0"
    v = round(v, 1)
    tens = hundreds = decimal = True
    if v >= 10: tens = False
    if v >= 100: hundreds = False
    #if v%1 != 0: decimal = False

    V = str(v)

    if tens:
        V = "00" + V
    elif hundreds:
        V = "0" + V
    #if decimal:
    #    V = V + ".0"
    
    return V


screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
main_surface = pygame.Surface((800, 600))
pygame.display.set_caption("Oil Drop Lab")
main_color = (30,30,30)
main_width = 800
main_height = 600
main_location = (0, 0)

pointer_shift = 1
shift_point_by = 0

voltage_string = "000.0"

paper = pygame.image.load("yellowpaper.jpg")
paper = pygame.transform.scale(paper, (.37*main_width, .65*main_height))

#setting
oil_types = ["Mineral Oil", "Xylene", "Water"]
oil_density = [830,870,1000]
oil_index = 2
plate_separation_mm = 5
drop_radius_um = 0
excess_electrons = 0


run = True
while run:

    info = pygame.display.Info()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            info = pygame.display.Info()
            x, y, main_width, main_height = ResizeMath(info.current_w, info.current_h)
            main_surface = pygame.Surface((main_width, main_height))
            main_location = (x,y)
            paper = pygame.transform.scale(pygame.image.load("yellowpaper.jpg"), (.37*main_width, .65*main_height))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if pointer_shift < 3:
                    pointer_shift += 1
            elif event.key == pygame.K_RIGHT:
                if pointer_shift > 0:
                    pointer_shift -= 1
            elif event.key == pygame.K_UP:
                if pointer_shift == 0: magnitude = .1
                elif pointer_shift == 1: magnitude = 1
                elif pointer_shift == 2: magnitude = 10
                elif pointer_shift == 3: magnitude = 100
                if float(voltage_string) + magnitude >= 999.9:
                    voltage_string = IntToString(999.9)
                else: voltage_string = IntToString(float(voltage_string)+magnitude)
            elif event.key == pygame.K_DOWN:
                if pointer_shift == 0: magnitude = .1
                elif pointer_shift == 1: magnitude = 1
                elif pointer_shift == 2: magnitude = 10
                elif pointer_shift == 3: magnitude = 100
                if float(voltage_string) - magnitude <= 0:
                    voltage_string = IntToString(0.0)
                else: voltage_string = IntToString(float(voltage_string)-magnitude)

            

    #Draw environment
    
    screen.fill((0,0,0))
    main_surface.fill(main_color)

        #Draw grid
    spacing = .05 * main_height
    start = spacing
    while start < main_height:
        pygame.draw.rect(main_surface, (75,75,75), pygame.Rect(0, start, main_width, .002*main_height))
        start += spacing
    spacing = .05 * main_height
    start = spacing
    while start < main_width:
        pygame.draw.rect(main_surface, (75,75,75), pygame.Rect(start, 0, .002*main_height, main_height))
        start += spacing

    
    pygame.draw.rect(main_surface, (10,10,10), pygame.Rect(main_width*.4, main_height*.85, main_width*.61, main_height*.16))
    
    pygame.draw.rect(main_surface, (150,150,150), pygame.Rect(main_width*.425, main_height*.1, main_width*.552, main_height*.05))
    pygame.draw.rect(main_surface, (150,150,150), pygame.Rect(main_width*.425, main_height*.7, main_width*.552, main_height*.05))


    power_supply_text = pygame.font.Font(None, int(.06*main_height)).render("Power Supply", True, (0,0,0))
    V_text = pygame.font.Font(None, int(.12*main_height)).render("V", True, (0,0,0))

    pygame.draw.rect(main_surface, (142, 90, 69), pygame.Rect((0, 0, main_width*.4, main_height)))
    
        #Power supply
    pygame.draw.rect(main_surface, (150,150,150), pygame.Rect(((main_width*.05)/2, main_height*.72, main_width*.35, main_height * .25)))
    pygame.draw.rect(main_surface, (10,10,10), pygame.Rect(((main_width*.085)/2, main_height*.787, main_width*.272, main_height * .16)))
    pygame.draw.circle(main_surface, (200,0,0), (.243*main_width, .9*main_height), .006*main_width)
    
    if pointer_shift == 0: shift_point_by = .259*main_width
    elif pointer_shift == 1: shift_point_by = .194*main_width
    elif pointer_shift == 2: shift_point_by = .1325*main_width
    elif pointer_shift == 3: shift_point_by = .068*main_width
    pygame.draw.polygon(main_surface, (200,0,0), [(shift_point_by, .8*main_height),(shift_point_by+.015*main_width, .81*main_height),(shift_point_by+.03*main_width, .8*main_height)])   
    pygame.draw.polygon(main_surface, (200,0,0), [(shift_point_by, .93*main_height),(shift_point_by+.015*main_width, .92*main_height),(shift_point_by+.03*main_width, .93*main_height)])


    #7 segment display surfaces
    tenths = pygame.Surface((.05*main_height, .09*main_height))
    tenths.fill((10,10,10))
    ones = pygame.Surface((.05*main_height, .09*main_height))
    ones.fill((10,10,10))
    tens = pygame.Surface((.05*main_height, .09*main_height))
    tens.fill((10,10,10))
    hundreds = pygame.Surface((.05*main_height, .09*main_height))
    hundreds.fill((10,10,10))

    DrawSegment(tenths, int(str(voltage_string)[4]), .05*main_height, .09*main_height)
    DrawSegment(ones, int(str(voltage_string)[2]), .05*main_height, .09*main_height)
    DrawSegment(tens, int(str(voltage_string)[1]), .05*main_height, .09*main_height)
    DrawSegment(hundreds, int(str(voltage_string)[0]), .05*main_height, .09*main_height)


    Notes_title_text = pygame.font.Font(None, int(.1*main_height)).render("Notes:", True, (0,0,0))
    Oil_type_text = pygame.font.Font(None, int(.058*main_height)).render("Liquid: "+oil_types[oil_index], False, (0,0,0))
    Oil_density_text = pygame.font.Font(None, int(.058*main_height)).render("Density = "+str(oil_density[oil_index])+"kg/m^3", False, (0,0,0))
    Plate_separation_text = pygame.font.Font(None, int(.058*main_height)).render("Plate Separation = "+str(plate_separation_mm)+"mm", False, (0,0,0))
    Radius_text = pygame.font.Font(None, int(.055*main_height)).render("Radius = "+str(drop_radius_um)+"um", False, (0,0,0))

    Positive_plate = pygame.font.Font(None, int(.09*main_height)).render("+  +  +  +  +  +  +  +  +  +", True, (255,0,0))
    Negative_plate = pygame.font.Font(None, int(.1*main_height)).render("_  _  _  _  _  _  _  _  _ ", True, (0,0,255))

    Controls_title = pygame.font.Font(None, int(.05*main_height)).render("Controls:", True, (255,255,255))
    Controls_line1 = pygame.font.Font(None, int(.04*main_height)).render("Arrow Keys --> Voltage     N --> New Drop", True, (255,255,255))
    Controls_line2 = pygame.font.Font(None, int(.04*main_height)).render("Z --> Zap Drop     M --> Open/Close Menu", True, (255,255,255))

    #Apply Surfaces
    main_surface.blit(power_supply_text, (main_width*.1, main_height*.735))
    main_surface.blit(V_text, (main_width*.324, main_height*.83))

        #7 segment display
    main_surface.blit(tenths, (.255*main_width, .821*main_height))
    main_surface.blit(ones, (.19*main_width, .821*main_height))
    main_surface.blit(tens, (.128*main_width, .821*main_height))
    main_surface.blit(hundreds, (.065*main_width, .821*main_height))

        #paper
    paper.blit(Notes_title_text, (.15*main_height, .05*main_height))
    paper.blit(Oil_type_text, (.025*main_height, .19*main_height))
    paper.blit(Oil_density_text, (.025*main_height, .3*main_height))
    paper.blit(Plate_separation_text, (.025*main_height, .4*main_height))
    paper.blit(Radius_text, (.025*main_height, .5*main_height))
    main_surface.blit(paper, (.015*main_width,.025*main_width))

        #plates text
    main_surface.blit(Positive_plate, (.45*main_width, .09*main_height))
    main_surface.blit(Negative_plate, (.455*main_width, .66*main_height))

    main_surface.blit(Controls_title, (.63*main_width, .86*main_height))
    main_surface.blit(Controls_line1, (.51*main_width, .91*main_height))
    main_surface.blit(Controls_line2, (.512*main_width, .95*main_height))

    screen.blit(main_surface, main_location)


    pygame.display.flip()

pygame.quit