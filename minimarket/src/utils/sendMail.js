import nodemailer from 'nodemailer';

const transporter = nodemailer.createTransport({
    host:'smtp.office365.com',
    port: 587,
    auth:{
        user: process.env.EMAIL_HOST_USER,
        pass: process.env.EMAIL_HOST_PASSWORD,
    },
});

export const enviarCorreoValidacion = async ({destino, hash}) => {
    const html = `
    <p>
        Hola para comenzar a disfrutar de todas las ofertas en nuestro Minimarket, por favor haz click en el siguiente enlace   
            <a href="${process.env.FRONTEND_URL}?hash=${hash}">
                Valida mi cuenta.
            </a>
    </p>`;

    try{
        const respuesta = await transporter.sendMail({
            from:'no-reply-innova@hotmail.com',
            to: destino,
            subject:'Validacion de cuenta de Minimarket APP',
            html
        });
        console.log('Correo enviado')
        return {
            message: 'Mail enviado correctamente',
            success: true,
            data: respuesta,
        };
    }catch(ex){
        console.log(ex)
        if (ex instanceof Error){
            return {
                message: 'Error al enviar el mail',
                success: false,
                error: ex.message,
            };
        } 
    }
}