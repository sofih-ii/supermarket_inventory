
import os
from django.core.management.base import BaseCommand
from excel_data.utils import update_master_excel

class Command(BaseCommand):
    help = 'Actualiza el archivo maestro de Excel con los datos más recientes'

    def handle(self, *args, **kwargs):
        inventory_file = '/home/sofihii/inventarios/inventario_24_06_2024.xlsx'
        master_file = '/home/sofihii/archivo_excel_maestro/maestro.xlsx'
        update_master_excel(inventory_file, master_file)
        self.stdout.write(self.style.SUCCESS('Se ha actualizado el archivo maestro de Excel con éxito.'))