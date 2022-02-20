# Import the "arcade" library
import arcade
arcade.open_window(800, 600, "pueblo")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 170, 0, arcade.color.BITTER_LIME)

# ---Empezemos a dibujar---

# DIBUJAMOS CASA GRANDE
arcade.draw_lrtb_rectangle_filled(100, 300, 400, 150, arcade.color.GOLDEN_YELLOW)
arcade.draw_triangle_filled(50, 400, 350, 400, 200, 550, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(240, 260, 530, 450, arcade.color.BROWN)


#  DIBUJAMOS VENTANA
arcade.draw_lrtb_rectangle_filled(110, 150, 380, 340, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(110, 150, 280, 240, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(250, 290, 280, 240, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(115, 145, 375, 345, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(115, 145, 275, 245, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(255, 285, 275, 245, arcade.color.WHITE)

# DIBUJAMOS PUERTAS
arcade.draw_lrtb_rectangle_filled(180, 220, 210, 152, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(260, 298, 360, 302, arcade.color.BROWN)

# DIBUJAMOS TERRAZA
arcade.draw_lrtb_rectangle_filled(100, 300, 320, 300, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(102, 150, 318, 302, arcade.color.GOLDEN_YELLOW)
arcade.draw_lrtb_rectangle_filled(152, 200, 318, 302, arcade.color.GOLDEN_YELLOW)
arcade.draw_lrtb_rectangle_filled(202, 250, 318, 302, arcade.color.GOLDEN_YELLOW)
arcade.draw_lrtb_rectangle_filled(252, 300, 318, 302, arcade.color.GOLDEN_YELLOW)

# COMPLETAR PUERTA TERAZA
arcade.draw_lrtb_rectangle_filled(260, 298, 318, 304, arcade.color.BROWN)

# DIBUJAMOS CASA PEQUEÑA
arcade.draw_lrtb_rectangle_filled(600, 730, 320, 150, arcade.color.GRAY)
arcade.draw_triangle_filled(550, 320, 780, 320, 665, 430, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(690, 715, 430, 380, arcade.color.BROWN)

# DIBUJAMOS PUERTA Y VENTANAS

arcade.draw_lrtb_rectangle_filled(605, 645, 310, 270, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(685, 725, 310, 270, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(610, 640, 305, 275, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(690, 720, 305, 275, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(650, 675, 210, 152, arcade.color.BROWN)

# DIBUJAMOS ARBOL GRANDE
arcade.draw_lrtb_rectangle_filled(400, 420, 210, 150, arcade.color.BROWN)
arcade.draw_triangle_filled(380, 200, 440, 200, 410, 390, arcade.color.GREEN)
# DIBUJAMOS ARBOL PEQUEÑO
arcade.draw_lrtb_rectangle_filled(500, 510, 180, 150, arcade.color.BROWN)
arcade.draw_triangle_filled(495, 175, 515, 175, 505, 280, arcade.color.GREEN)

# DIBUJAMOS EL SOL
arcade.draw_circle_filled(720, 560, 30, arcade.color.YELLOW)

# DIBUJAMOS EL COCHE
arcade.draw_lrtb_rectangle_filled(340, 560, 120, 80, arcade.color.RED)
arcade.draw_polygon_filled([[370, 120],
                            [385, 155],
                            [500, 155],
                            [520, 120]],
                            arcade.color.RED)

arcade.draw_circle_filled(400, 80, 26, arcade.color.BLACK)
arcade.draw_circle_filled(400, 80, 10, arcade.color.WHITE)
arcade.draw_circle_filled(500, 80, 26, arcade.color.BLACK)
arcade.draw_circle_filled(500, 80, 10, arcade.color.WHITE)



arcade.draw_polygon_filled([[373, 120],
                            [387, 152],
                            [448, 152],
                            [448, 120]],
                            arcade.color.YELLOW)

arcade.draw_polygon_filled([[452, 120],
                            [452, 152],
                            [498, 152],
                            [518, 120]],
                            arcade.color.YELLOW)


# --- cuadro acabado ---
arcade.finish_render()

# manten la ventana abierta hsata que lo cierre
arcade.run()