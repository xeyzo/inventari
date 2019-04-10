from django.contrib import admin
from .models import *
import csv
from django.http import HttpResponse


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"



class SpamAdmin(admin.ModelAdmin):
    readonly_fields = ('get_c',)
    fields = ('a', 'b', 'get_c')

    def get_c(self, obj):
        return obj.a + obj.b


class PegawaiAdmin (admin.ModelAdmin, ExportCsvMixin):
    list_display = ['id_pegawai','nama_pegawai','nip','alamat']
    list_filter = ('id_pegawai','nip')
    actions = ["export_as_csv"]
    search_fields = ['id_pegawai','nama_pegawai','nip']
    list_per_page = 10

admin.site.register(Pegawai, PegawaiAdmin)

class PeminjamanAdmin (admin.ModelAdmin):
    list_display = ['id_peminjaman','tanggal_pinjam','tanggal_kembali','status_peminjaman']
    list_filter = ()
    search_field = ['id_peminjaman']
    list_per_page = 10

admin.site.register(Peminjaman, PeminjamanAdmin)

class PetugasAdmin (admin.ModelAdmin):
    list_display = ['id_petugas','nama_petugas']
    list_filter = ()
    search_field = ['nama_petugas']
    list_per_page = 10

admin.site.register(Petugas, PetugasAdmin)

class DetailAdmin (admin.ModelAdmin):
    list_display = ['id_detail_pinjam','id_inventaris','jumlah']
    list_filter = ()
    search_field = ['id_detail_pinjam']
    list_per_page = 10


admin.site.register(Detail_pinjam, DetailAdmin)

class InventarisAdmin (admin.ModelAdmin):
    list_display = ['id_inventaris','nama','kondisi','keterangan','jumlah','id_jenis','tanggal_register','kode_inventaris','id_petugas']
    list_filter = ()
    search_field = ['id_inventaris', 'nama']
    list_per_page = 10

admin.site.register(Inventaris, InventarisAdmin)

class JenisAdmin (admin.ModelAdmin):
    list_display = ['id_jenis','nama_jenis','kode_jenis','keterangan']
    list_filter = ()
    search_field = ['id_jenis','nama_jenis','kode_jenis']
    list_per_page = 10

admin.site.register(Jenis, JenisAdmin)

class RuangAdmin (admin.ModelAdmin):
    list_display = ['id_ruang','nama_ruang','kode_ruang','keterangan']
    list_filter = ()
    search_field = ['id_ruang','nama_ruang','kode_ruang']
    list_per_page = 10

admin.site.register(Ruang, RuangAdmin)




