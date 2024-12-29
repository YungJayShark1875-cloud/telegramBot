from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace this with your bot's API token
TOKEN = "7861802284:AAF_doskNoDcE9OvTKjsiS8dRd-zc42RkDA"

# Store user state
user_states = {}

# Command: Start
async def start(update, context):
    await update.message.reply_text("Hello! I am your bot. Use /help to see available commands.")

# Command: Help
async def help_command(update, context):
    await update.message.reply_text(
        "Here are the commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Show help message\n"
        "/race - Get race basics"
    )

# Command: Race
async def race(update, context):
    user_id = update.effective_user.id
    user_states[user_id] = "awaiting_race_selection"  # Set user state
    await update.message.reply_text(

        "Please select a race:\n"
        "1. European\n"
        "2. EuroAsian\n"
        "3. Asian\n"
        "4. American\n"
        "5. African"
    )

# Handle Race Basics
async def handle_basics(update, context):
    user_id = update.effective_user.id

    # Check if the user is in the correct state
    if user_states.get(user_id) != "awaiting_race_selection":
        return  # Ignore if user is not in the right state

    datas = [
        {"Name": "Vlad", "Age": 43, "House": "Petrovs"},
        {"Name": "Smith", "Age": 23, "House": "Lancasters"},
        {"Name": "Joma", "Age": 76, "House": "Luo"},
        {"Name": "Nuria", "Age": 43, "House": "Garcia"},
        {"Name": "James", "Age": 43, "House": "Obi"},
    ]

    user_message = update.message.text.strip()
    if user_message == "1":
        await update.message.reply_text(f"Here are the basics for European race: {datas[0]}")
    elif user_message == "2":
        await update.message.reply_text(f"Here are the basics for EuroAsian race: {datas[1]}")
    elif user_message == "3":
        await update.message.reply_text(f"Here are the basics for Asian race: {datas[2]}")
    elif user_message == "4":
        await update.message.reply_text(f"Here are the basics for American race: {datas[3]}")
    elif user_message == "5":
        await update.message.reply_text(f"Here are the basics for African race: {datas[4]}")
    else:
        await update.message.reply_text("Invalid selection. Please select a valid option.")
        return

    # Clear user state after successful response
    user_states.pop(user_id, None)

# Handle regular messages
async def handle_message(update, context):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

# Error Handler
async def error_handler(update, context):
    print(f"An error occurred: {context.error}")

# Main function to start the bot
def main():
    # Build the application
    app = ApplicationBuilder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("race", race))

    # Register a single message handler for handling race basics
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_basics))

    # Register error handler
    app.add_error_handler(error_handler)

    print("Bot is running...")

    # Start polling with drop_pending_updates=True
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
