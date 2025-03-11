import { createContext, useState, useContext, SetStateAction, useEffect } from 'react';

const AuthContext = createContext<{
  user: IUser | null;
  login: (userData: SetStateAction<IUser | null>) => void;
  logout: () => void;
}>({
  user: null,
  login: () => {},
  logout: () => {}
});

import { ReactNode } from 'react';
import IUser from '../interfaces/IUser';

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<IUser | null>({username:"", password:""});
  useEffect(() => {
    if (user) {
      localStorage.setItem('user', JSON.stringify(user));
    } else {
      localStorage.removeItem('user');
    }
  }, [user]);
  const login = (userData: SetStateAction<IUser | null>) => {
    setUser(userData);
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}