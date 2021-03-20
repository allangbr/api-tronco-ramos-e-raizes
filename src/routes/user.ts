import { Router } from 'express'

import UserController from '../controllers/UserController'
import auth from '../middlewares/auth'

const userRoutes = Router()
const userController = new UserController()

userRoutes.use(auth)

userRoutes.post('/:id', userController.create)
userRoutes.get('/', userController.index)
userRoutes.put('/:id', userController.update)
userRoutes.delete('/:id', userController.destroy)
userRoutes.patch('/:id', userController.enableIsSuper)

export default userRoutes
