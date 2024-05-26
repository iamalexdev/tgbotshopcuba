import telebot

# Reemplaza TOKEN con el token de acceso de tu bot
TOKEN = '7155702952:AAGCIt4vZymsd-8wv-zPgmKsI1Y2d3MT1kg'

# Lista de usuarios VIP
vip_users = ['@Alex_GlezRM', '@RagnaLTB',]

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.reply_to(message,"❇️ Bienvenido al VIP Manager de 🇨🇺 𝑮𝒂𝒎𝒊𝒏𝒈 𝑺𝒉𝒐𝒑𝑪𝒖𝒃𝒂.\n✅ Esperamos sea de tu agrado nuestro servicio.\n✅Si buscas información VIP para realizar algún intercambio o deseas convertirte en uno de ellos estás en el lugar correcto.\nℹ️ Para más información contactar a @RagnaLTB")

@bot.message_handler(commands=['vip'])
def handle_vip_command(message):
    # Obtener el username del usuario que realiza la consulta
    requester_username = f"@{message.from_user.username}"
    
    args = message.text.split()
    
    # Verificar si se proporcionó un username
    if len(args) > 1:
        mentioned_user = args[1]
        
        if mentioned_user in vip_users:
            bot.reply_to(message, f"👨🏻‍💻 Hola {requester_username}\n\n👤 El Usuario: {mentioned_user}\n✅ Es VIP en la Federación 🇨🇺 𝑮𝒂𝒎𝒊𝒏𝒈 𝑺𝒉𝒐𝒑𝑪𝒖𝒃𝒂")
        else:
            bot.reply_to(message, f"⚠️ Alerta {requester_username} ⚠️\n\n👤 El Usuario: {mentioned_user}\n❌ No es VIP en la Federación 🇨🇺 𝑮𝒂𝒎𝒊𝒏𝒈 𝑺𝒉𝒐𝒑𝑪𝒖𝒃𝒂.\n🔰 Puede que tenga algunas referencias positivas en el grupo \n\n🙏🏻 Aconsejamos que solo realicen negocios con MIEMBROS VIP.")
    else:
        bot.reply_to(message, f"⚠️ Alerta {requester_username} ⚠️\n\n✅ Debes proporcionar un username después del comando /vip.")

bot.infinity_polling()



