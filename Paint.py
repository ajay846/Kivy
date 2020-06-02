from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class Draw(Widget):

    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=3)

    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        print("RELEASED!",touch)


class SimplePaintTool(App):

    def build(self):
        return Draw()

if __name__ == "__main__":
    SimplePaintTool().run()
