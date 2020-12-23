class Road:

    def __init__(self, i_length, i_width):
        self._m_len = i_length
        self._m_wid = i_width

    def Realise(self, mass, sm):
        print(f"Для покрытия дороги нужно ({self._m_len * self._m_wid * mass * sm / 1000} т.)")


Road(20, 5000).Realise(25, 5)
Road(300, 200).Realise(35, 40)
Road(250, 400).Realise(50, 60)
