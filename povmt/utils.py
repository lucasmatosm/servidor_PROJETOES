
def instance_of(instancia, nome_classe):
    return instancia.__class__.__name__ == nome_classe


def download_path(instance, filename):

    diretorio = "media/No-img.jpg"

    if instance_of(instance, "Atividade"):
        diretorio = "user_{0}/{1}".format(instance.id_usuario.id, filename)


    return diretorio


