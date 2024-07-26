from django.contrib import admin

from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # essa list_display deixa a tabela no django admin organizada por cada coluna  
    list_display = 'id','first_name','last_name','phone'
    # ordenado por
    ordering = 'id',
    # exibir ordem de data de criacao
    #list_filter = 'create_date',
    search_fields = 'id','first_name','last_name',
    # lista por pagina
    list_per_page = 10
    # maximo para mostrar
    list_max_show_all = 20
    list_editable = 'first_name', 'last_name',
    # campos que voce clica e vai para a area de atualizar contato
    list_display_links = 'id','phone',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    # essa list_display deixa a tabela no django admin organizada por cada coluna  
    list_display = 'name'
    # ordenado por
    ordering = 'id',