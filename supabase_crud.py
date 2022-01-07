from supabase_client import Client
from dotenv import dotenv_values
import asyncio

def db_init():

    config = dotenv_values(".env")
    supa_db = Client( 
        api_url=config.get("SUPABASE_URL"),
        api_key=config.get("SUPABASE_KEY")
    )

    return supa_db


async def db_create(data_2_insert):

    result=[]
    db_config=db_init()
    failure, success = await (
        db_config.table("network_info")
        .insert(data_2_insert)
    )
    result.append(failure)
    result.append(success)
    
    return result
    

async def db_read():

    result=[]
    db_config=db_init()
    failure, success = await (
    db_config.table("network_info")
        .select("id,ip_address")
        .limit(4)
        .query()
    )

    result.append(failure)
    result.append(success)
    
    return result

async def db_update(selection_crit,data_2_update):

    result=[]
    db_config=db_init()
    failure, success = await (
    db_config.table("cities")
        .update(
      	selection_crit,
      	data_2_update)
    )

    result.append(failure)
    result.append(success)
    
    return result


if __name__ == "__main__":
    print("entered the program")
    config = dotenv_values(".env")

    data=[{"ip_address": "192.168.1.5"}]
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # create_result=asyncio.run(supabase_insert(data))
    # print(create_result)
    # read_result=asyncio.run(db_read())
    # print(read_result)
    update_result=asyncio.run(db_update({'id':'3'},{'ip_address':'192.168.1.3'}))
    print(update_result)