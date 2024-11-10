"use client";
import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  ReactNode,
  useCallback,
} from "react";

interface Palette {
  color1: string;
  color2: string;
  color3: string;
  color4: string;
  id: string;
}

interface PalettesContextType {
  palettes: Palette[];
  addPalette: (palette: Palette) => void;
  deletePalette: (id: string) => void;
  errorMessage: string | null; // New error message property
}

const PalettesContext = createContext<PalettesContextType | undefined>(
  undefined
);

export const usePalettes = (): PalettesContextType => {
  const context = useContext(PalettesContext);
  if (!context) {
    throw new Error("usePalettes must be used within a PalettesProvider");
  }
  return context;
};

interface PalettesProviderProps {
  children: ReactNode;
}

const PalettesProvider: React.FC<PalettesProviderProps> = ({ children }) => {
  const [palettes, setPalettes] = useState<Palette[]>([]);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  useEffect(() => {
    const savedPalettes = localStorage.getItem("palettes");
    if (savedPalettes) {
      setPalettes(JSON.parse(savedPalettes));
    }
  }, []);

  const addPalette = useCallback(
    (newPalette: Palette) => {
      const duplicate = palettes.some(
        (palette) =>
          palette.color1 === newPalette.color1 &&
          palette.color2 === newPalette.color2 &&
          palette.color3 === newPalette.color3 &&
          palette.color4 === newPalette.color4
      );

      if (duplicate) {
        setErrorMessage("This palette has already been added.");
      } else {
        const updatedPalettes = [...palettes, newPalette];
        setPalettes(updatedPalettes);
        localStorage.setItem("palettes", JSON.stringify(updatedPalettes));
        setErrorMessage(null); // Reset error message on successful addition
      }
    },
    [palettes]
  );

  const deletePalette = useCallback(
    (id: string) => {
      const updatedPalettes = palettes.filter((palette) => palette.id !== id);
      setPalettes(updatedPalettes);
      localStorage.setItem("palettes", JSON.stringify(updatedPalettes));
    },
    [palettes]
  );

  return (
    <PalettesContext.Provider
      value={{ palettes, addPalette, deletePalette, errorMessage }}
    >
      {children}
    </PalettesContext.Provider>
  );
};

export default PalettesProvider;
