from app import app, db

# Ensure app is properly configured before creating the context
# For example, make sure you have set the database URI, etc.

# Create the application context
with app.app_context():
    # Now you are within the application context
    db.create_all()
    print("Database tables created successfully!")

