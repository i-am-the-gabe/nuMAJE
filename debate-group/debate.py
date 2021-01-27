from debate_class import *

@bot.group()
async def debate(ctx):
    if ctx.invoked_subcommand is None or ctx.invoked_subcommand is "help":
        embed = discord.Embed(title="Debate Help", description="List of commands for the Debate category:",colour=red)
        embed.add_field(name="`new`", value="Allows you to start a new debate. `debate new Coke vs. Pepsi` allows you to start a debate about 'Coke vs. Pepsi', for example.", inline=False)
        embed.add_field(name="`add`", value="Allows you to add a user to the debate. `debate add 1 @king gman, slayer of caps-lock` allows you to add <@418867304982380554> to Debate 1, for example.", inline=False)
        embed.add_field(name="`check`", value="Allows you to check how many debates are happening, and their id. `debate check`.", inline=False)
        await ctx.send(embed=embed)

@debate.command()
async def new(ctx, *, topic: str):
    topic_already = False

    for i in current_debates:
        if i.topic == topic:
            topic_already = True
            break
    if topic_already:
        await ctx.send("A debate about that topic is already in the list.")
    else:
        await ctx.send(f"A new debate has started about: {topic}.")
        current_debates.append(DebateTemplate(topic))

@debate.command()
@has_permissions(manage_messages=True)
async def delete(ctx, slot):
    slot = int(slot)-1 
    await ctx.send(f"Debate with topic {current_debates[slot].topic} has been deleted.")
    del current_debates[slot]

@debate.command()
async def check(ctx):
    index = 0
    if current_debates is not []:
        for i in current_debates:
            debate_embed = discord.Embed(title=f"{str(index+1)}. {i.topic}", description="Being debated by:", colour=red)
            if i.participants is not []:
                for j in i.participants:
                    debate_embed.description += f" <@{j.id}>"
            else:
                debate_embed.description = " It seems that no one is currently debating this."

            await ctx.send(embed=debate_embed)
            index += 1
    else:
        await ctx.send(f"No debates are happening right now, <@{ctx.author.id}>. If you want to start one, use `debate new [your topic]`. ")

@debate.command()
async def add(ctx, slot, added : discord.Member):
    selected = current_debates[int(slot)-1] 
    if added not in selected.participants:
        selected.participants.append(added)

        for i in current_debates:
            await ctx.send(i.participants)

    else:
        await ctx.send("Sorry, that person is already debating this.")
