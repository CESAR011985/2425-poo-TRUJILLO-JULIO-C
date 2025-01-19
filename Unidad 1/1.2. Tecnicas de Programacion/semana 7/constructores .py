# Programa en Python que gestiona implementos de soldadura mediante el uso de constructores (__init__) y destructores (__del__)

class WeldingSupplies:
    """
    Clase para gestionar implementos de soldadura.
    - El constructor (__init__) inicializa los atributos con las cantidades de cada implemento.
    - El destructor (__del__) realiza una limpieza al liberar los recursos.
    """

    def __init__(self, electrodes_kg, cutting_discs_units, paint_canisters):
        """
        Constructor que inicializa los implements de soldadura.
        :param electrodes_kg: Cantidad de electrodos en kilogramos.
        :param cutting_discs_units: Número de discos de corte.
        :param paint_canisters: Número de canecas de pintura.
        """
        self.electrodes_kg = electrodes_kg
        self.cutting_discs_units = cutting_discs_units
        self.paint_canisters = paint_canisters
        print(f"[INFO] Implementos inicializados: {self.electrodes_kg} kg de electrodos, {self.cutting_discs_units} discos de corte, {self.paint_canisters} canecas de pintura.")

    def use_supplies(self, electrodes_used, discs_used, paint_used):
        """
        Método para simular el uso de los implementos.
        :param electrodes_used: Kilogramos de electrodos usados.
        :param discs_used: Número de discos usados.
        :param paint_used: Número de canecas de pintura usadas.
        """
        if electrodes_used <= self.electrodes_kg:
            self.electrodes_kg -= electrodes_used
            print(f"[INFO] Se usaron {electrodes_used} kg de electrodos. Restan {self.electrodes_kg} kg.")
        else:
            print("[ERROR] No hay suficientes electrodos disponibles.")

        if discs_used <= self.cutting_discs_units:
            self.cutting_discs_units -= discs_used
            print(f"[INFO] Se usaron {discs_used} discos de corte. Restan {self.cutting_discs_units} unidades.")
        else:
            print("[ERROR] No hay suficientes discos de corte disponibles.")

        if paint_used <= self.paint_canisters:
            self.paint_canisters -= paint_used
            print(f"[INFO] Se usaron {paint_used} canecas de pintura. Restan {self.paint_canisters} canecas.")
        else:
            print("[ERROR] No hay suficientes canecas de pintura disponibles.")

    def __del__(self):
        """
        Destructor que realiza una limpieza al eliminar el objeto.
        """
        print("[INFO] Recursos de implementos de soldadura liberados.")

# Demostración del uso de la clase WeldingSupplies
if __name__ == "__main__":
    # Crear un objeto WeldingSupplies con cantidades iniciales
    supplies = WeldingSupplies(electrodes_kg=20, cutting_discs_units=100, paint_canisters=2)

    # Usar algunos implementos
    supplies.use_supplies(electrodes_used=5, discs_used=20, paint_used=1)

    # Intentar usar más implementos de los disponibles
    supplies.use_supplies(electrodes_used=30, discs_used=50, paint_used=3)

    # El destructor se activará automáticamente al finalizar el programa
    print("[INFO] Finalizando el programa. Los recursos se liberarán automáticamente.")
