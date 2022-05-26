/* import moralis */
const Moralis = require("moralis/node");

/* Moralis init code */
const serverUrl = "https://y1iny6rhtmyq.usemoralis.com:2053/server";
const appId = "UQ6INdIpjNlfoDI56fDQlA3AHpfRnJRXwd8s2jLM";
const masterKey = "r2NsZxUy9ATThSyb69LqXAtZc1KJBc5hOiKoNHNo";

await Moralis.start({ serverUrl, appId, masterKey });

function foo {
    const options = { chain: "bsc", block_number_or_hash: "2" };

    // get block content on BSC
    const transactions = await Moralis.Web3API.native.getBlock(options);
}
