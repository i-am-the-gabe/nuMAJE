@bot.command()
async def wiki(ctx, *, args):
    try:
        contents = wikipedia.page(args)
        description = contents.summary
        chars = len(description)

        if chars >= 1300:
            description = description[:1300]
            chars = len(description)
            description = description + "..."

        disclaimer, value, final_text = "From Wikipedia:", str(chars) + " characters in total.", description

        wikipedia_embed = discord.Embed(title=contents.title,
                                        description=description,
                                        url=contents.url,
                                        colour=red)

        wikipedia_embed.add_field(name="Tip",
                                  value="Click on the title of this message to be redirected to the Wikipedia article about _" + contents.title + "_.",
                                  inline=True)
        wikipedia_embed.add_field(name="From Wikipedia:", value=value, inline=True)

        await ctx.send(embed=wikipedia_embed)

    except wikipedia.DisambiguationError as e:
        try:
            disambiguation_error_embed = discord.Embed(title="Multiple Pages Found", 
                                                       description='\n'.join(map(str, e.options)) + "\n \n \n **Type one of these instead.**", colour=red)

            await ctx.send(embed=disambiguation_error_embed)

        except wikipedia.PageError:
            await ctx.send("That page doesn't exist, sorry.")
