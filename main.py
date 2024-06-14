import kivy

kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp

class TestApp(App):

    def animate(self, instance):

        if not hasattr(self.root, 'label'):
            self.root.label = Label(text='Move me!', size_hint=(None, None), size=(100, 50), y=0)
            self.root.add_widget(self.root.label)
            self.root.label_moving_up = False


        target_y = self.root.height - self.root.label.height if not self.root.label_moving_up else 0


        animation = Animation(y=target_y, duration=1, t='out_bounce')

        # Применяем анимацию к Label и переключаем состояние перемещения
        animation.start(self.root.label)
        self.root.label_moving_up = not self.root.label_moving_up

    def build(self):
        # Создаем корневой виджет FloatLayout
        layout = FloatLayout()

        # Создаем кнопку и привязываем метод animate() как обработчик нажатия
        button = Button(size_hint=(None, None), text='Поменять позицию текста', on_press=self.animate,
                        pos_hint={'center_x': .5, 'y': 0}, width=len('Поменять позицию текста') * dp(10), height=dp(40))
        button.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        layout.add_widget(button)

        return layout


if __name__ == '__main__':
    TestApp().run()