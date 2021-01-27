def generate_session_id():
    nuMAJE_id = uuid.uuid1()
    return str(nuMAJE_id)

bot_id = generate_session_id()

@bot.command()
async def check_id(ctx):
    """
    Sends the current bot_id to the user.
    """
    await ctx.send(bot_id)

@bot.command()
@has_permissions(administrator=True)
async def kill_id(ctx, nuMAJE_id):
    """
    Kills with id.
    """

    if nuMAJE_id == bot_id:

        embed=discord.Embed(title="nuMAJE has been turned off.", description="Command called by " + str(ctx.author) +".", colour=red)

        embed.add_field(name="nuMAJE id: ", value=str(bot_id))
        channel = bot.get_channel(729117784184979487)
        await channel.send(embed=embed)

        quit()
