const APP_ID = "2a437b8895d249889b9ba902153f6bc5"
const CHANNEL = "main"
const TOKEN = "0062a437b8895d249889b9ba902153f6bc5IABhVw6jxziIxvu+Q+LQp3PJm5dt8d1rWg4fU+pg5bo/umTNKL8AAAAAEAA5DUG6Oo5/YgEAAQA6jn9i"

const client = AgoraRTC.createClient({mode:'rtc',codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStreams = async () => {
    await client.join(APP_ID,CHANNEL,TOKEN,null)
}