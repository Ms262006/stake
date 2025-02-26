from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the Stake Mine Prediction Bot! Use /help to get instructions.")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""
    To use the prediction feature, format your input as follows:
    /predict <stake_amount>, <duration_in_days>, <interest_rate_percentage>
    Example: /predict 1000, 5, 3
    """)

def predict(update: Update, context: CallbackContext):
    try:
        if len(context.args) != 3:
            raise ValueError("You must provide exactly 3 values: <stake_amount>, <duration_in_days>, <interest_rate_percentage>")
        
        stake_amount = float(context.args[0])
        duration = int(context.args[1])
        interest_rate = float(context.args[2])
        
        prediction_outcome = stake_amount * (1 + interest_rate / 100) ** duration
        confidence_level = "High"  
        recommendations = "Consider increasing stake for better returns."
        
        response = f"""
**Prediction Outcome:**
- Estimated Outcome: {prediction_outcome:.2f} units
- Confidence Level: {confidence_level}
- Recommendations: {recommendations}
        """
        update.message.reply_text(response)
    
    except ValueError as e:
        update.message.reply_text(f"Error: {e}. Please provide valid data in the correct format.")

def main():
    updater = Updater("YOUR_BOT_API_KEY", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("predict", predict))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

