const { exec } = require('child_process');

module.exports = (req, res) => {
    exec('python acp.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            res.status(500).json({ error: 'Internal Server Error' });
            return;
        }
        console.log(`stdout: ${stdout}`);
        console.error(`stderr: ${stderr}`);
        res.status(200).json({ message: 'Script executed successfully.' });
    });
};
