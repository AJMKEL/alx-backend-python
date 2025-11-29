import asyncio
import aiosqlite


async def async_fetch_users():
    """
    Asynchronously fetch all users from the database
    
    Returns:
        list: All users from the users table
    """
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        print(f"Fetched {len(results)} users")
        return results


async def async_fetch_older_users():
    """
    Asynchronously fetch users older than 40 from the database
    
    Returns:
        list: Users older than 40
    """
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > ?", (40,))
        results = await cursor.fetchall()
        print(f"Fetched {len(results)} users older than 40")
        return results


async def fetch_concurrently():
    """
    Execute multiple database queries concurrently using asyncio.gather
    
    Returns:
        tuple: Results from both queries (all_users, older_users)
    """
    # Run both queries concurrently
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    
    print("\nAll Users:")
    for user in all_users:
        print(user)
    
    print("\nUsers Older Than 40:")
    for user in older_users:
        print(user)
    
    return all_users, older_users


if __name__ == "__main__":
    # Run the concurrent fetch
    asyncio.run(fetch_concurrently())
